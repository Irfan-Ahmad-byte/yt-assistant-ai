import { callAPI } from './callAPI';

async function userNotificationsAPI(profile: any) {
  const success = await callAPI({
    method: 'POST',
    path: '/notifications',
    data: {
        username: profile.login,
        email: profile.email,
        full_name: profile.full_name,
    },
    apiUrlEnvVariable: 'NOTIFICATIONS_API_URL',
    apiKeyEnvVariable: 'NOTIFICATIONS_API_KEY',
  });

  if (!success) {
    console.error("Failed to send user notifications data to the backend API");
  }

  return success;
}
