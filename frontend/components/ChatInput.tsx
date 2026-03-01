"use client"

import { useState } from "react"

type Props = {
  onSend: (text: string) => void
  loading: boolean
}

export default function ChatInput({ onSend, loading }: Props) {
  const [input, setInput] = useState("")

  function handleSend() {
    if (!input.trim() || loading) return
    onSend(input.trim())
    setInput("")
  }

  function handleKeyDown(e: React.KeyboardEvent) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="flex gap-2 py-4 border-t border-gray-800">
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Ask a cooking question..."
        disabled={loading}
        className="flex-1 bg-gray-800 text-white rounded-xl px-4 py-2 text-sm outline-none placeholder-gray-500 disabled:opacity-50"
      />
      <button
        onClick={handleSend}
        disabled={loading || !input.trim()}
        className="bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white rounded-xl px-4 py-2 text-sm font-medium transition-colors"
      >
        Send
      </button>
    </div>
  )
}