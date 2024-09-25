export const metadata = {
  title: "Home - Simple",
  description: "Page description",
};

import UrlInput from "@/components/url_input";
import TextInput from "@/components/text_input";
import ResponseBox from "@/components/response_box";

export default function Home() {
  return (
    <>
      <UrlInput />
      <div className="flex flex-col justify-between w-full h-full">
        <ResponseBox />
        <TextInput />
      </div>
    </>
  );
}
