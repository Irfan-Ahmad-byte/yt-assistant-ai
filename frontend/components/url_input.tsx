"use client"

import { useState } from 'react';
import { Button, Field, Input } from '@headlessui/react';
import clsx from 'clsx';
import Social from './ui/social';
import IntroBox from './intro_box';
import { sendUrl, ApiResponse } from './api_client/api';


export default function UrlInput(): JSX.Element {
  const [inputUrl, setInputUrl] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);

  const handleSend = async (): Promise<void> => {
    if (!inputUrl) {
      alert('Please enter a URL');
      return;
    }

    setLoading(true);
    try {
      const response: ApiResponse = await sendUrl(inputUrl);

      // Handle success response
      if (response && response.id) {
        document.cookie = `transcription_id=${response.id}; path=/; max-age=${7 * 24 * 60 * 60}`; // Expires in 7 days
        alert('ID saved in cookies successfully'); // Show success message
      }
    } catch (error) {
      console.error('Error sending URL:', error);
      alert('Something went wrong. Please try again.'); // Show error message to user
    } finally {
      setLoading(false);
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

      <div className="w-full max-w-md px-4">
        <IntroBox />
      </div>

      <div className="w-full max-w-md px-4">
        <Social border={false} />
      </div>
    </div>
  );
}
