import axios from "axios";

const axiosInstance = axios.create({
  baseURL: process.env.REACT_APP_PLANT_SWAP_API
});

export default axiosInstance;
