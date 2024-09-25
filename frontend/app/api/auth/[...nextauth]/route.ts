import NextAuth from "next-auth";
import type { AuthOptions } from "next-auth";
import GithubProvider from "next-auth/providers/github";

export const authOptions: AuthOptions = {
  providers: [
    GithubProvider({
      clientId: process.env.GITHUB_ID as string,
      clientSecret: process.env.GITHUB_SECRET as string,
    }),
  ],

  callbacks: {
    async signIn({user, account, profile, email, credentials}) {
      let creds = credentials;
      console.log("signIn", creds);
      return true;
    },
    async session({session, user, token}) {

      let email = session.user?.email;
      
      console.log("session", email);
      return session;
    },
    async jwt({token, user, account, profile}) {
      console.log("jwt", {token, user, account, profile});
      return token;
    },
  }
};

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };


