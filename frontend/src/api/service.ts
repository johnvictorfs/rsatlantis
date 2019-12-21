import { Api } from '@/api'

export default class Service {
  public api: Api

  constructor(api: Api) {
    this.api = api
  }
}
