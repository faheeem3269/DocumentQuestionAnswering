// features/file/fileSlice.js
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  file: null,
  previewUrl: null,
};

const file = createSlice({
  name: "file",
  initialState,
  reducers: {
    setFile(state, action) {
      state.file = action.payload.file;
      state.previewUrl = action.payload.previewUrl;
    },
    clearFile(state) {
      state.file = null;
      state.previewUrl = null;
    },
  },
});

export const { setFile, clearFile } = file.actions;
export default file.reducer;
