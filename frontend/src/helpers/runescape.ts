import api from '../api'

export async function isInClan(player?: string): Promise<boolean> {
  // const { data } = await api({
  //   url: `http://services.runescape.com/m=website-data/playerDetails.ws?names=%5B%22${player}%22%5D&callback=jQuery000000000000000_0000000000&_=0`,
  //   headers: {},
  //   method: 'get'
  // })
  if (player) {
    const { data } = await api.get(`http://services.runescape.com/m=website-data/playerDetails.ws?names=%5B%22${player}%22%5D&callback=jQuery000000000000000_0000000000&_=0`)
    return data.clan === 'Atlantis'
  }
  return false
}
