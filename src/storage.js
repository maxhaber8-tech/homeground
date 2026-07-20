// localStorage-backed shim matching the window.storage API the game uses.
// Note: everything (including the "shared" leaderboard) is per-browser here.
// Swap this file for a real backend if you want a global leaderboard.
if (!window.storage) {
  const k = (key, shared) => (shared ? 'hg:shared:' : 'hg:me:') + key
  window.storage = {
    async get(key, shared = false) {
      const v = localStorage.getItem(k(key, shared))
      if (v === null) throw new Error('Key not found: ' + key)
      return { key, value: v, shared }
    },
    async set(key, value, shared = false) {
      localStorage.setItem(k(key, shared), value)
      return { key, value, shared }
    },
    async delete(key, shared = false) {
      localStorage.removeItem(k(key, shared))
      return { key, deleted: true, shared }
    },
    async list(prefix = '', shared = false) {
      const p = k(prefix, shared)
      const keys = []
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i)
        if (key.startsWith(p)) keys.push(key.slice(k('', shared).length))
      }
      return { keys, prefix, shared }
    },
  }
}
