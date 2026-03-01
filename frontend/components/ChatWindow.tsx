"use client"

import { useEffect, useRef } from "react"
import type { Message } from "@/app/page"
import MessageBubble from "./MessageBubble"

type Props = {
  messages: Message[]
  loading: boolean
}

export default function ChatWindow({ messages, loading }: Props) {
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages])

  return (
    <div className="flex-1 overflow-y-auto py-4">
      {messages.length === 0 && (
        <p className="text-center text-gray-500 mt-20">
          Ask me anything about cooking!
        </p>
      )}
      {messages.map((msg, i) => (
        <MessageBubble key={i} message={msg} />
      ))}
      {loading && (
        <div className="flex justify-start mb-3">
          <div className="bg-gray-800 text-gray-400 rounded-2xl rounded-bl-none px-4 py-2 text-sm">
            Thinking...
          </div>
        </div>
      )}
      <div ref={bottomRef} />
    </div>
  )
}