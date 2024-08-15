// import Footer from "./Footer";
// import Header from "./Header";
// import ProductCard from "./ProductCard";

// const Shop = () => {
//   return (
//     <div>
//       <Header />
//       <div className="bg-gradient-to-r from-purple-500 to-indigo-500 py-32">
//         <h1 className="text-6xl text-center font-extrabold text-white drop-shadow-lg">
//           Our Products
//         </h1>
//         <div className="flex flex-wrap justify-center gap-8 mt-16 px-8 md:px-16 lg:px-24">
//           <ProductCard />
//         </div>
//       </div>
//       <Footer />
//     </div>
//   );
// };

// export default Shop;


import { useDispatch } from "react-redux";
import Footer from "./Footer";
import Header from "./Header";
import ProductCard from "./ProductCard";

const Shop = () => {
  // Assume we have a list of products
  const dispatch = useDispatch()
  const products = [
    { id: 1, name: "Organic Fertilizer", description: "Description 1", price: 500, image: "https://cdn.cdnparenting.com/articles/2021/07/16191322/380433403.webp" },
    { id: 2, name: "Crops Seed", description: "Description 2", price: 700, image: "https://articles-1mg.gumlet.io/articles/wp-content/uploads/2016/12/seeds.jpg?compress=true&quality=80&w=640&dpr=2.6" },
    // Add more products as needed
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow">
        <div className="bg-gradient-to-r from-purple-600 to-indigo-600 py-20">
          <h1 className="text-5xl md:text-6xl text-center font-extrabold text-white drop-shadow-lg">
            Our Products
          </h1>
        </div>
        <div className="container mx-auto px-4 py-16">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
            {products.map((product) => (
              <ProductCard key={product.id} productData={product} />
            ))}
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default Shop;