"use client"

import { useState } from "react"
import ChatWindow from "@/components/ChatWindow"
import ChatInput from "@/components/ChatInput"
import { sendMessage } from "@/lib/api"

export type Message = {
  role: "user" | "assistant"
  content: string
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([])
  const [loading, setLoading] = useState(false)

  async function handleSend(text: string) {
    const userMessage: Message = { role: "user", content: text }
    setMessages(prev => [...prev, userMessage])
    setLoading(true)

    try {
      const response = await sendMessage(text)
      const assistantMessage: Message = { role: "assistant", content: response }
      setMessages(prev => [...prev, assistantMessage])
    } catch (error) {
      const errorMessage: Message = {
        role: "assistant",
        content: "Something went wrong. Is the backend running?"
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="flex flex-col h-screen max-w-3xl mx-auto px-4">
      <h1 className="text-2xl font-bold py-4 border-b border-gray-800">
        🍳 Recipe Assistant
      </h1>
      <ChatWindow messages={messages} loading={loading} />
      <ChatInput onSend={handleSend} loading={loading} />
    </main>
  )
}