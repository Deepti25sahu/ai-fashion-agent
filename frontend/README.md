# AI Fashion Shopping Agent

An intelligent AI-powered fashion ecommerce assistant that helps users discover stylish products using conversational search, outfit recommendations, smart filtering, and premium shopping experience.

---

# Problem Statement

Traditional ecommerce platforms often provide overwhelming shopping experiences where users must manually browse hundreds of products, apply multiple filters, compare items individually, and still struggle to find the perfect fashion products.

Most online shopping platforms rely heavily on keyword-based search systems, which fail to understand the actual intent, styling preferences, occasions, or fashion aesthetics users are looking for.

For example, when a user searches:

- “black dress for farewell”
- “streetwear oversized hoodie”
- “casual airport outfit”

traditional systems simply match keywords instead of understanding fashion intent, occasion, style preferences, or outfit compatibility.

This creates several problems:

- Poor product discovery experience
- Too many irrelevant results
- No styling guidance
- Difficult product comparison
- Lack of personalization
- Time-consuming browsing process
- Decision fatigue for users

The goal of this project is to solve these challenges using AI-driven conversational ecommerce.

AI Fashion Shopping Agent transforms traditional ecommerce into an intelligent shopping assistant that:

- understands natural language fashion queries
- recommends stylish products intelligently
- suggests matching outfits
- explains recommendation reasoning
- helps compare products
- provides a clean path toward purchase

The project demonstrates how conversational AI can significantly improve user experience in modern ecommerce systems.

---

# Key Features

## AI Fashion Search

Users can search using conversational queries such as:

- black dress for farewell
- oversized korean hoodie
- pink heels for party
- airport casual outfit

---

## Outfit Recommendation Engine

The AI suggests complementary outfit items dynamically.

Example:
- sneakers
- jackets
- accessories
- handbags

---

## Product Recommendation System

Products are ranked intelligently based on:
- relevance
- ratings
- fashion matching
- recommendation logic

---

## Product Comparison

Users can compare products side-by-side for smarter purchasing decisions.

---

## Wishlist System

Products can be saved locally using browser localStorage.

---

## Voice Search

Speech recognition support allows voice-based fashion search.

---

## Dark Mode

Premium luxury dark/light theme support.

---

## Smart Follow-Up Questions

The AI asks contextual questions like:
- What occasion is this for?
- Casual or formal?
- Preferred color?

---

## Recommendation Reasoning

Each product contains AI-generated reasoning explaining why it was recommended.

---

# Tech Stack

## Frontend

- Next.js 14
- TypeScript
- Tailwind CSS
- Framer Motion
- Lucide Icons

## Backend

- FastAPI
- Python

## APIs

- SerpAPI

## Installation

### Frontend

npm install
npm run dev

### Backend

pip install -r requirements.txt
uvicorn main:app --reload

## Deployment Links

Frontend:
https://ai-fashion-agent-ecru.vercel.app/

Backend:
https://ai-fashion-agent.onrender.com

## GitHub Repository

https://github.com/Deepti25sahu/ai-fashion-agent

---



This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
