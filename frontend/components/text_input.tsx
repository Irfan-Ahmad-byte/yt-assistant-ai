"use client"


import React, { useState, useRef } from 'react';
import { Button, Field, Input, Textarea } from '@headlessui/react';
import clsx from 'clsx';
import Social from './ui/social';
import IntroBox from './intro_box';
import { sendUrl, streamQuestion } from './api_client/api';

export default function Example(): JSX.Element {
  const [inputUrl, setInputUrl] = useState<string>('');
  const [question, setQuestion] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [streamingMessage, setStreamingMessage] = useState<string>('');
  const responseBoxRef = useRef<HTMLDivElement | null>(null);

  const handleSend = async (): Promise<void> => {
    if (!inputUrl) {
      alert('Please enter a URL');
      return;
    }

    setLoading(true);
    try {
      const response = await sendUrl(inputUrl);

      if (response && response.id) {
        document.cookie = `transcription_id=${response.id}; path=/; max-age=${7 * 24 * 60 * 60}`; // Save in cookies for 7 days
        alert('ID saved in cookies successfully');
      }
    } catch (error) {
      console.error('Error sending URL:', error);
      alert('Something went wrong. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleQuestionSend = async (): Promise<void> => {
    const id = document.cookie
      .split('; ')
      .find((row) => row.startsWith('transcription_id='))
      ?.split('=')[1];

    if (!id) {
      alert('ID not found. Please submit the URL first.');
      console.error('ID not found in cookies');
      return;
    }

    if (!question) {
      alert('Please enter a question');
      return;
    }

    setStreamingMessage(''); // Reset the message before new streaming starts
    try {
      await streamQuestion(id, question, (newMessage) => {
        setStreamingMessage(newMessage);
        if (responseBoxRef.current) {
          responseBoxRef.current.scrollTop = responseBoxRef.current.scrollHeight; // Auto-scroll
        }
      });
    } catch (error) {
      console.error('Error while streaming:', error);
      alert('Something went wrong while streaming the response.');
    }
  };

  return (
    <div className="flex flex-col justify-between h-full">
      <div className="w-full max-w-md px-12 mt-10">
        <Field className="flex items-center">
          <Input
            className={clsx(
              'block w-full rounded-l-lg border-none bg-white/5 py-1.5 px-3 text-sm/6 text-white',
              'focus:outline-none data-[focus]:outline-2 data-[focus]:-outline-offset-2 data-[focus]:outline-white/25',
              'h-12'
            )}
            placeholder="Paste the URL of the YouTube Video."
            value={inputUrl}
            onChange={(e) => setInputUrl(e.target.value)}
          />
          <Button
            className="inline-flex items-center gap-2 rounded-r-lg bg-gray-700 py-1.5 px-3 text-sm/6 font-semibold text-white shadow-inner shadow-white/10 focus:outline-none data-[hover]:bg-gray-600 data-[open]:bg-gray-700 data-[focus]:outline-1 data-[focus]:outline-white h-12"
            onClick={handleSend}
            disabled={loading}
          >
            {loading ? 'Sending...' : 'Send'}
          </Button>
        </Field>
      </div>

      <div className="w-full max-w-full px-7 mb-10">
        <Field className="flex items-center">
          <Textarea
            className={clsx(
              'block w-full resize-none rounded-l-lg border-none bg-white/5 px-3 text-sm/6 text-white',
              'focus:outline-none data-[focus]:outline-2 data-[focus]:-outline-offset-2 data-[focus]:outline-white/25',
              'h-12'
            )}
            rows={1}
            placeholder="Ask your questions related to the YouTube Video."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <Button
            className="inline-flex items-center gap-2 rounded-r-lg bg-gray-700 px-3 text-sm/6 font-semibold text-white shadow-inner shadow-white/10 focus:outline-none data-[hover]:bg-gray-600 data-[open]:bg-gray-700 data-[focus]:outline-1 data-[focus]:outline-white h-12"
            onClick={handleQuestionSend}
          >
            Send
          </Button>
        </Field>
      </div>

      <div className="w-full max-w-full px-7 mt-10" ref={responseBoxRef}>
        <Field disabled>
          <Textarea
            className={clsx(
              'mt-3 block w-full resize-none rounded-lg border-none bg-white/5 py-1.5 px-3 text-sm/6 text-white',
              'focus:outline-none data-[focus]:outline-2 data-[focus]:-outline-offset-2 data-[focus]:outline-white/25',
              'h-96 max-h-96'
            )}
            rows={3}
            value={streamingMessage}
            readOnly
          />
        </Field>
      </div>

      <div className="w-full max-w-md px-4">
        <IntroBox />
      </div>

      <div className="w-full max-w-md px-4">
        <Social border={false} />
      </div>
    </div>
  );
}
