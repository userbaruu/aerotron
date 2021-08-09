import axios from "axios"
import {Cookies} from "quasar"

export async function getBarangAction (ctx, {page}) {
  const header = Cookies.get("_msk")

  return await axios.get(
    `${window.location.protocol}//${process.env.REST_HOST}/stok/api/barang/`,
    {
      headers: { authorization: `Bearer ${header}` },
      params: { pages: page != null ? page : null }
    }
  )
}
