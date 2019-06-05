import api from '../api';

type Player = {
  isSuffix: boolean;
  recruiting: boolean;
  name: string;
  clan: string;
  title: string;
};

export async function isInClan(player: Player) {
  return new Promise(async (resolve, reject) => {
    try {
      const { data } = await api({
        url: `http://services.runescape.com/m=website-data/playerDetails.ws?names=%5B%22${player}%22%5D&callback=jQuery000000000000000_0000000000&_=0`,
        headers: {},
        method: 'get'
      });
      resolve(data.clan === 'Atlantis');
    } catch (error) {
      reject(error);
    }
  });
}
