"use client";

import Image from "next/image";

import { Heart } from "lucide-react";

interface Props {

  product: any;

  addToWishlist: any;
}

export default function ProductCard({

  product,

  addToWishlist

}: Props) {

  return (

    <div className="
      bg-white
      rounded-3xl
      overflow-hidden
      shadow-xl
      hover:scale-105
      transition
      duration-300
    ">

      <div className="
        relative
        w-full
        h-72
      ">

        <Image

          src={
            product.image
            ||
            "https://picsum.photos/400/500"
          }

          alt={product.name || "Fashion"}

          fill

          className="
            object-cover
          "

          unoptimized
        />

      </div>

      <div className="p-5">

        <h2 className="
          font-bold
          text-lg
          text-black
        ">
          {product.name}
        </h2>

        <p className="
          text-pink-600
          font-bold
          mt-2
        ">
          {product.price}
        </p>

        <p className="
          text-gray-500
          text-sm
        ">
          ⭐ {product.rating}
        </p>

        <p className="
          text-gray-400
          text-sm
        ">
          {product.source}
        </p>

        <div className="
          flex
          gap-2
          mt-4
        ">

          <a

            href={product.link}

            target="_blank"

            rel="noopener noreferrer"

            className="
              bg-black
              text-white
              px-4
              py-2
              rounded-xl
              flex-1
              text-center
            "
          >
            Buy Now
          </a>

          <button

            onClick={() =>
              addToWishlist(product)
            }

            className="
              bg-pink-500
              text-white
              p-3
              rounded-xl
            "
          >
            <Heart size={18} />
          </button>

        </div>

      </div>

    </div>
  );
}