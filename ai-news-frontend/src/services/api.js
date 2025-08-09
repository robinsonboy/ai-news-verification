const API_BASE_URL = 
  process.env.NODE_ENV === 'production'
    ? window.location.origin + '/api'
    : 'http://localhost:5001/api'

export const fetchNews = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/news`)
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    return data.data
  } catch (error) {
    console.error("Error fetching news:", error)
    throw error
  }
}

export const fetchStatistics = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/statistics`)
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    return data.data
  } catch (error) {
    console.error("Error fetching statistics:", error)
    throw error
  }
}

export const submitNews = async (newsData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/news/submit`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newsData),
    })
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    return data
  } catch (error) {
    console.error("Error submitting news:", error)
    throw error
  }
}

