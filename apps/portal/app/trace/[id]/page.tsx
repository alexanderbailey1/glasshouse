interface Props {
  params: { id: string }
}

export default async function TracePage({ params }: Props) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_REASON_API}/trace/${params.id}`, { cache: 'no-store' })
  const data = await res.json()
  return (
    <div style={{ padding: 20 }}>
      <pre>{JSON.stringify(data, null, 2)}</pre>
      <a href="/">Back</a>
    </div>
  )
}
