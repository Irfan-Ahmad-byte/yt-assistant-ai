'use client';


import React, { useState } from 'react';

const StreamedResponseComponent: React.FC = () => {
  // Define the state type as an array of strings
  const [tokens, setTokens] = useState<string[]>([]);

  const handleStreamResponse = async () => {
    try {
      const response = await fetch("http://backend-address/agent/ask?query=12hello", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "X-Api-Key": "my-api-key",
        },
      });

      if (!response.body) {
        throw new Error('ReadableStream not supported or empty response');
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let done = false;

      while (!done) {
        const { value, done: readerDone } = await reader.read();
        done = readerDone;

        // Decode the bytes into a string
        const chunk = decoder.decode(value, { stream: true });

        // Split the chunk into tokens by spaces (or adjust this as needed)
        const newTokens = chunk.split(/\s+/);

        // Update the tokens state to reflect new tokens received
        setTokens((prevTokens) => [...prevTokens, ...newTokens]);
      }
    } catch (error) {
      console.error("Error while streaming:", error);
    }
  };

  return (
    <div>
      <h2>Streaming Response:</h2>
      <button onClick={handleStreamResponse}>Start Streaming</button>
      <div>
        {tokens.map((token, index) => (
          <p key={index}>Token {index + 1}: {token}</p>
        ))}
      </div>
    </div>
  );
};

export default StreamedResponseComponent;
