"use client";

import type { NextRequest } from "next/server";
import { signIn, useSession } from "next-auth/react";
import { redirect } from "next/navigation";

import Login from "@/components/auth/login";


export default function LogIn() {
  return (
    <>
      <Login />
    </>
  );
}
