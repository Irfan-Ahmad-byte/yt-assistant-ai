import { callAPI } from './callAPI';

async function userAuthAPI(profile: any) {
  const success = await callAPI({
    method: 'POST',
    path: '/user',
    data: {
      username: profile.login,
      email: profile.email,
      full_name: profile.full_name,
    },
    apiUrlEnvVariable: 'AUTH_API_URL',
    apiKeyEnvVariable: 'AUTH_API_KEY',
  });

  if (!success) {
    console.error("Failed to send user data to the backend API");
  }

  return success;
}
