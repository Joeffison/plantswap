import apiClient from "./client"

export  const getPlant = ({ plant_id }) => {
  return apiClient.get(`/plants/${plant_id}`)
}
