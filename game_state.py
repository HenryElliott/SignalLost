class Memory:
    def __init__(self, id, text, emotional_weight=1):
        self.id = id
        self.text = text
        self.emotional_weight = emotional_weight
        self.held = False
        self.remembered = False

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "emotional_weight": self.emotional_weight,
            "held": self.held,
            "remembered": self.remembered,
        }

    @staticmethod
    def from_dict(data):
        m = Memory(data['id'], data['text'], data['emotional_weight'])
        m.held = data.get('held', False)
        m.remembered = data.get('remembered', False)
        return m

class PlayerState:
    def __init__(self):
        self.current_scene = 'ruined_city_intro'
        self.memories = {}
        self.emotional_weight = 0

    def to_dict(self):
        return {
            "current_scene": self.current_scene,
            "memories": {mid: mem.to_dict() for mid, mem in self.memories.items()},
            "emotional_weight": self.emotional_weight,
        }

    @staticmethod
    def from_dict(data):
        state = PlayerState()
        state.current_scene = data.get('current_scene', 'ruined_city_intro')
        mems = data.get('memories', {})
        for mid, mdict in mems.items():
            state.memories[mid] = Memory.from_dict(mdict)
        state.emotional_weight = data.get('emotional_weight', 0)
        return state

    def add_memory(self, memory):
        self.memories[memory.id] = memory
        if memory.held or memory.remembered:
            self.emotional_weight += memory.emotional_weight

    def remove_memory(self, memory_id):
        mem = self.memories.get(memory_id)
        if mem:
            if mem.held or mem.remembered:
                self.emotional_weight -= mem.emotional_weight
            del self.memories[memory_id]
