// relative path which gets resolved by nginx proxy
const SERVER_URL = "/api";

/**
 * Helper function for API requests.
 * @param {string} endpoint - The API endpoint (e.g., "/total-revenue").
 * @param {Object} options - Fetch options (e.g., method, headers, body).
 * @returns {Promise<any>} - The JSON response.
 */
export async function apiFetch(endpoint, options = {}) {
  const url = `${SERVER_URL}${endpoint}`;

  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  } catch (error) {
    console.error(`Error fetching ${endpoint}:`, error);
    throw error;
  }
}
