interface Props {

  wishlist: any[];
}

export default function WishlistDrawer({

  wishlist

}: Props) {

  return (

    <div className="
      px-10
      py-10
    ">

      <h2 className="
        text-3xl
        font-bold
        mb-6
      ">
        Wishlist ❤️
      </h2>

      <div className="
        flex
        gap-4
        overflow-x-auto
      ">

        {wishlist.map(
          (item, index) => (

            <img

              key={index}

              src={item.image}

              className="
                w-32
                h-40
                object-cover
                rounded-xl
              "
            />
          )
        )}

      </div>

    </div>
  );
}