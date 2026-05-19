"use client";

import { useState, useEffect } from "react";

import { motion } from "framer-motion";

import {
  Mic,
  Moon,
  Sun
} from "lucide-react";

import Navbar from "../components/Navbar";

import ProductCard from "../components/ProductCard";

import SearchBar from "../components/SearchBar";

import OutfitSuggestions from "../components/OutfitSuggestions";

import WishlistDrawer from "../components/WishlistDrawer";

import Footer from "../components/Footer";

export default function Home() {

  // ===========================================
  // STATES
  // ===========================================

  const [message, setMessage] =
    useState("");

  const [reply, setReply] =
    useState("");

  const [products, setProducts] =
    useState<any[]>([]);

  const [outfit, setOutfit] =
    useState<any[]>([]);

  const [wishlist, setWishlist] =
    useState<any[]>([]);

  const [darkMode, setDarkMode] =
    useState(false);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");

  const [sortOption, setSortOption] =
    useState("default");

  const [selectedColor, setSelectedColor] =
    useState("all");

  // ===========================================
  // LOAD WISHLIST
  // ===========================================

  useEffect(() => {

    const savedWishlist =
      localStorage.getItem(
        "wishlist"
      );

    if (savedWishlist) {

      setWishlist(
        JSON.parse(savedWishlist)
      );
    }

  }, []);

  // ===========================================
  // SAVE WISHLIST
  // ===========================================

  useEffect(() => {

    localStorage.setItem(

      "wishlist",

      JSON.stringify(wishlist)
    );

  }, [wishlist]);

  // ===========================================
  // SEARCH FUNCTION
  // ===========================================

  const sendMessage = async (
    customMessage?: string
  ) => {

    try {

      setLoading(true);

      setError("");

      const searchText =
        customMessage || message;

      const res = await fetch(

        "http://127.0.0.1:8000/chat",

        {
          method: "POST",

          headers: {
            "Content-Type":
            "application/json",
          },

          body: JSON.stringify({
            message: searchText,
          }),
        }
      );

      const data =
        await res.json();

      setReply(
        data.reply || ""
      );

      setProducts(
        data.products || []
      );

      setOutfit(
        data.outfit || []
      );

      setLoading(false);

    } catch (err) {

      console.log(err);

      setError(
        "Failed to fetch products"
      );

      setLoading(false);
    }
  };

  // ===========================================
  // WISHLIST
  // ===========================================

  const addToWishlist = (
    product: any
  ) => {

    const exists =
      wishlist.find(

        (item) =>
          item.link === product.link
      );

    if (!exists) {

      setWishlist([
        ...wishlist,
        product
      ]);
    }
  };

  // ===========================================
  // VOICE SEARCH
  // ===========================================

  const startVoiceSearch = () => {

    const SpeechRecognition =

      (window as any)
        .SpeechRecognition ||

      (window as any)
        .webkitSpeechRecognition;

    if (!SpeechRecognition) {

      alert(
        "Voice search not supported"
      );

      return;
    }

    const recognition =
      new SpeechRecognition();

    recognition.start();

    recognition.onresult =
      (event: any) => {

        const transcript =
          event.results[0][0]
            .transcript;

        setMessage(transcript);
      };
  };

  // ===========================================
  // SORT PRODUCTS
  // ===========================================

  const sortedProducts =
    [...products];

  if (sortOption === "low-high") {

    sortedProducts.sort(
      (a, b) => {

        const priceA =
          parseInt(

            a.price?.replace(
              /[^0-9]/g,
              ""
            )

          ) || 0;

        const priceB =
          parseInt(

            b.price?.replace(
              /[^0-9]/g,
              ""
            )

          ) || 0;

        return priceA - priceB;
      }
    );
  }

  if (sortOption === "high-low") {

    sortedProducts.sort(
      (a, b) => {

        const priceA =
          parseInt(

            a.price?.replace(
              /[^0-9]/g,
              ""
            )

          ) || 0;

        const priceB =
          parseInt(

            b.price?.replace(
              /[^0-9]/g,
              ""
            )

          ) || 0;

        return priceB - priceA;
      }
    );
  }

  // ===========================================
  // COLOR FILTER
  // ===========================================

  const filteredProducts =

    selectedColor === "all"

      ?

      sortedProducts

      :

      sortedProducts.filter(

        (product) => {

          const productName =

            product.name
              ?.toLowerCase()

              .replace(/-/g, "")

              .replace(/\s+/g, "")

              .replace(/[^a-z]/g, "");

          const filterValue =

            selectedColor
              .toLowerCase()

              .replace(/\s+/g, "")

              .replace(/[^a-z]/g, "");

          return (
            productName.includes(
              filterValue
            )
          );
        }
      );

  // ===========================================
  // UI
  // ===========================================

  return (

    <div className={

      darkMode

        ?

        "bg-black text-white min-h-screen"

        :

        "bg-gradient-to-br from-pink-100 via-purple-100 to-pink-200 min-h-screen"

    }>

      {/* NAVBAR */}

      <Navbar />

      {/* HERO */}

      <section className="
        text-center
        py-20
        px-6
      ">

        <motion.h1

          initial={{
            opacity: 0,
            y: -40
          }}

          animate={{
            opacity: 1,
            y: 0
          }}

          transition={{
            duration: 0.7
          }}

          className="
            text-6xl
            font-black
            mb-6
            bg-gradient-to-r
            from-pink-500
            to-purple-600
            bg-clip-text
            text-transparent
          "
        >
          AI Fashion Shopping Agent
        </motion.h1>

        <p className="
          text-xl
          max-w-2xl
          mx-auto
          opacity-80
        ">
          Discover luxury fashion,
          AI-powered outfit ideas,
          and premium shopping vibes ✨
        </p>

      </section>

      {/* SEARCH */}

      <div className="
        max-w-4xl
        mx-auto
        px-6
      ">

        <SearchBar

          message={message}

          setMessage={setMessage}

          sendMessage={sendMessage}
        />

        {/* ACTION BUTTONS */}

        <div className="
          flex
          flex-wrap
          justify-center
          gap-4
          mt-6
        ">

          {/* VOICE SEARCH */}

          <button

            onClick={startVoiceSearch}

            className="
              flex
              items-center
              gap-2
              bg-black
              text-white
              px-5
              py-3
              rounded-full
              hover:scale-105
              transition
            "
          >
            <Mic size={18} />

            Voice Search
          </button>

          {/* DARK MODE */}

          <button

            onClick={() =>
              setDarkMode(
                !darkMode
              )
            }

            className="
              flex
              items-center
              gap-2
              bg-white
              text-black
              px-5
              py-3
              rounded-full
              hover:scale-105
              transition
            "
          >

            {

              darkMode

                ?

                <Sun size={18} />

                :

                <Moon size={18} />
            }

            {

              darkMode

                ?

                "Light"

                :

                "Dark"
            }

          </button>

        </div>

      </div>

      {/* REPLY */}

      {reply && (

        <div className="
          text-center
          mt-10
          text-xl
          font-semibold
          px-6
        ">
          {reply}
        </div>
      )}

      {/* OUTFIT */}

      <OutfitSuggestions

        outfit={outfit}

        sendMessage={sendMessage}
      />

      {/* FILTERS */}

      <div className="
        flex
        flex-wrap
        justify-between
        items-center
        gap-4
        px-10
        mt-10
      ">

        {/* SORT */}

        <select

          value={sortOption}

          onChange={(e) =>
            setSortOption(
              e.target.value
            )
          }

          className="
            px-4
            py-3
            rounded-xl
            bg-white
            text-black
          "
        >

          <option value="default">
            Sort By
          </option>

          <option value="low-high">
            Price Low → High
          </option>

          <option value="high-low">
            Price High → Low
          </option>

        </select>

        {/* COLOR FILTER */}

        <div className="
          flex
          flex-wrap
          gap-3
        ">

          <button
            onClick={() =>
              setSelectedColor("all")
            }
            className="
              px-4
              py-2
              rounded-full
              bg-black
              text-white
            "
          >
            All
          </button>

          <button
            onClick={() =>
              setSelectedColor("black")
            }
            className="
              px-4
              py-2
              rounded-full
              bg-black
              text-white
            "
          >
            Black
          </button>

          <button
            onClick={() =>
              setSelectedColor("white")
            }
            className="
              px-4
              py-2
              rounded-full
              bg-white
              border
              text-black
            "
          >
            White
          </button>

          <button
            onClick={() =>
              setSelectedColor("pink")
            }
            className="
              px-4
              py-2
              rounded-full
              bg-pink-500
              text-white
            "
          >
            Pink
          </button>

          <button
            onClick={() =>
              setSelectedColor("blue")
            }
            className="
              px-4
              py-2
              rounded-full
              bg-blue-500
              text-white
            "
          >
            Blue
          </button>

          <button
            onClick={() =>
              setSelectedColor("red")
            }
            className="
              px-4
              py-2
              rounded-full
              bg-red-500
              text-white
            "
          >
            Red
          </button>

          <button
            onClick={() =>
              setSelectedColor("tshirt")
            }
            className="
              px-4
              py-2
              rounded-full
              bg-purple-500
              text-white
            "
          >
            T-Shirts
          </button>

        </div>

      </div>

      {/* LOADING */}

      {loading && (

        <div className="
          text-center
          py-20
          text-2xl
          font-bold
        ">

          Searching Fashion Products...

        </div>
      )}

      {/* ERROR */}

      {error && (

        <div className="
          text-center
          py-10
          text-red-500
          font-semibold
        ">

          {error}

        </div>
      )}

      {/* PRODUCTS */}

      <div className="
        grid
        grid-cols-1
        md:grid-cols-2
        lg:grid-cols-3
        xl:grid-cols-4
        gap-8
        px-10
        py-14
      ">

        {filteredProducts.map(

          (
            product,
            index
          ) => (

            <ProductCard

              key={index}

              product={product}

              addToWishlist={
                addToWishlist
              }
            />
          )
        )}

      </div>

      {/* EMPTY STATE */}

      {

        !loading

        &&

        filteredProducts.length === 0

        &&

        (

          <div className="
            text-center
            py-20
            text-2xl
            opacity-70
          ">

            No matching products found ✨

          </div>
        )
      }

      {/* WISHLIST */}

      <WishlistDrawer
        wishlist={wishlist}
      />

      {/* FOOTER */}

      <Footer />

    </div>
  );
}