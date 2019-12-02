import axios, { AxiosInstance } from 'axios'

import GuideService from './guides'
import UserService from './users'
import PlayerService from './players'

export class Api {
  public axios: AxiosInstance
  public baseURL: string = process.env.VUE_APP_API_URL || ''
  public guides: GuideService
  public users: UserService
  public players: PlayerService

  constructor() {
    // Full config:  https://github.com/axios/axios#request-config
    this.axios = axios.create({
      baseURL: this.baseURL + '/api' || '',
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken'
    })

    this.guides = new GuideService(this)
    this.users = new UserService(this)
    this.players = new PlayerService(this)

    this.setupMiddleware()
  }

  public async static(path: string) {
    /**
     * Access backend static files
     */
    return this.axios.get(`${this.baseURL}/static/${path}`)
  }

  private setupMiddleware(): void {
    /**
     * Setup API Middlewares
     */
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

    this.axios.interceptors.request.use(async config => {
      const token = localStorage.getItem('TOKEN')

      if (token) {
        config.headers.Authorization = `Token ${token}`
      }

      return config
    })
  }
}

export default new Api()

