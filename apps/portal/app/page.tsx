'use client'
import { useState } from 'react'

export default function Home() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')
  const [traceId, setTraceId] = useState<number | null>(null)
  const [citations, setCitations] = useState<string[]>([])

  const ask = async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_REASON_API}/ask`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    })
    const data = await res.json()
    setAnswer(data.answer)
    setCitations(data.citations)
    setTraceId(data.trace_id)
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>GlassHouse</h1>
      <textarea value={question} onChange={e => setQuestion(e.target.value)} />
      <br />
      <button onClick={ask}>Ask</button>
      {answer && (
        <div>
          <h2>Answer</h2>
          <p>{answer}</p>
          <ul>
            {citations.map(c => (
              <li key={c}>{c}</li>
            ))}
          </ul>
          {traceId && <a href={`/trace/${traceId}`}>View Trace</a>}
        </div>
      )}
    </div>
  )
}
