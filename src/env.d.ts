/// <reference types="astro/client" />
declare namespace App {
  interface Locals {
    cfContext?: { waitUntil(p: Promise<unknown>): void };
  }
}
declare const __BUILD_ID__: string;
