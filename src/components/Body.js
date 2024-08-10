import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Browse from "./Browse";
import Login from "./Login";
import Home from "./Home";
import { YieldAnalysis } from "./YieldAnalysis";
import Shop from "./Shop";

const Body = () => {
  const appRouter = createBrowserRouter([
    {
      path: "/",
      element: <Home />,
      children: [
        {
          path: "/browse",
          element: <Browse />,
        },
        {
          path: "/yield-analysis",
          element: <YieldAnalysis />,
        },
        {
          path: "/shop",
          element: <Shop />,
        },
        // {
        //   path: "/login",
        //   element: <Login />,
        // },
      ],
    },
  ]);
  return (
    <div>
      <RouterProvider router={appRouter} />
    </div>
  );
};

export default Body;
