// store.js
import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../redux/files/file";

export const store = configureStore({
  reducer: {
    file: userReducer,
  },
});
