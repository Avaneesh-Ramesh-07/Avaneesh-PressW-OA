export async function sendMessage(message: string): Promise<string> {
  const response = await fetch("http://127.0.0.1:8000/query", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  })

  if (!response.ok) {
    throw new Error("Failed to reach backend")
  }

  const data = await response.json()
  return data.response
}