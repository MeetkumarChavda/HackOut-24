import { useDispatch, useSelector } from "react-redux";
import ProductCard from "./ProductCard";
import { clearCart, removeFromCart } from "../redux/cartSlice";

const Cart = () => {
  const cartItem = useSelector((store) => store.cart);
  const dispatch = useDispatch();
  const handleClearCart = () => {
    dispatch(clearCart());
  };
  const deleteCartItem = (cartitem) => {
    dispatch(removeFromCart(cartitem));
  };
  return (
    <div>
      <div>
        {cartItem.map((cartitem) => (
          <div>
            <ProductCard productData={cartitem} cartState={false} />
            <button onClick={() => deleteCartItem(cartitem)}>
              <i className="fa-solid fa-trash"></i>
            </button>
          </div>
        ))}
      </div>
      <button
        className="p-3 text-md font-semibold bg-red-500"
        onClick={handleClearCart}
      >
        Clear Cart
      </button>
    </div>
  );
};

export default Cart;
