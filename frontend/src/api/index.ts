import axios, { AxiosInstance } from 'axios'

class Api {
  public axios: AxiosInstance
  public baseURL: string = process.env.VUE_APP_API_URL || ''

  constructor() {
    // Full config:  https://github.com/axios/axios#request-config
    this.axios = axios.create({
      baseURL: this.baseURL + '/api' || '',
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken'
    })


    this.middleware()
  }

  public async static(url: string) {
    /**
     * Access backend static files
     */
    return this.axios.get(this.baseURL + '/static/' + url)
  }

  private middleware(): void {
    this.axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*'

    this.axios.interceptors.request.use((response: any) => {
      if (!response.url.includes('static')) {
        // Add '/' to end of API url to avoid issues with running into the catch-all
        // url that goes to the frontend Vue app instead of the API
        if (response.url[response.url.length - 1] !== '/') {
          response.url += '/'
        }
      }
      return response
    })
    this.axios.interceptors.request.use(response => response, error => Promise.reject(error))
    this.axios.interceptors.response.use(response => response, error => Promise.reject(error))

    if (localStorage.getItem('TOKEN')) {
      this.axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('TOKEN')}`
    }
  }
}

const api = new Api()

export default api.axios

export { api }
