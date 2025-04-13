// api.ts
export interface ApiResponse {
  transcription: string;
  id: string;
}

export async function sendUrl(url: string): Promise<ApiResponse> {
  const targetUrl = process.env.NEXT_PUBLIC_API_URL as string; // URL from environment variables
  const response = await fetch(targetUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Api-Key': process.env.NEXT_PUBLIC_API_KEY as string, // API key from env
    },
    body: JSON.stringify({ url }),
  });
  if (!response.ok) {
    throw new Error('Failed to send URL');
  }
  return response.json();
}

export async function streamQuestion(id: string, question: string, onTokenReceived: (token: string) => void): Promise<void> {
  const targetUrl = `${process.env.NEXT_PUBLIC_QUESTION_API_URL}/${id}/${encodeURIComponent(question)}`;

  const response = await fetch(targetUrl, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'X-Api-Key': process.env.NEXT_PUBLIC_API_KEY as string,
    },
  });

  if (!response.ok || !response.body) {
    throw new Error('Failed to stream the response');
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let done = false;
  let message = '';

  while (!done) {
    const { value, done: readerDone } = await reader.read();
    done = readerDone;

    const chunk = decoder.decode(value, { stream: true });
    message += chunk;

    // Pass the new combined message to the callback function
    onTokenReceived(message);
  }
}
