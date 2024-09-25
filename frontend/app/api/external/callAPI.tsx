type Method = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';

interface APIRequestOptions {
  method: Method;
  path: string;
  pathArgs?: { [key: string]: any };
  data?: { [key: string]: any };
  apiUrlEnvVariable: string; // Env variable for the base API URL
  apiKeyEnvVariable: string; // Env variable for the API key
}

export async function callAPI({
  method,
  path,
  pathArgs = {},
  data = {},
  apiUrlEnvVariable,
  apiKeyEnvVariable,
}: APIRequestOptions) {
  // Construct the full URL with path arguments
  let url = process.env[apiUrlEnvVariable] as string;
  if (!url) {
    throw new Error(`Environment variable for API URL (${apiUrlEnvVariable}) is not set`);
  }

  Object.keys(pathArgs).forEach((key) => {
    const value = encodeURIComponent(pathArgs[key]);
    path = path.replace(`:${key}`, value);
  });
  url += path;

  // Set headers
  const headers: HeadersInit = {
    'Content-Type': 'application/json',
    'X-API-Key': process.env[apiKeyEnvVariable] as string, // API key from environment variable
  };

  // Make the API request
  const res = await fetch(url, {
    method,
    headers,
    body: method !== 'GET' ? JSON.stringify(data) : undefined, // GET requests typically do not send a body
  });

  // Handle response
  if (!res.ok) {
    console.error(`Failed to call API: ${url}`);
    return false;
  }

  return true;
}
