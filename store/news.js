export const state = () => ({
    listNews: [],
    currentOffset: 0,
    pageSize: 5
})

export const mutations = {
    setState (state, params) {
        const keys = Object.keys(params)
        keys.forEach(key => (state[key] = params[key]))
    }
}

export const actions = {
    getListNews(
        { dispatch, commit },
        { currentOffset, pageSize }
    )   {
        let url = 'https://newsapi.org/v2/everything'
        url += '?q=apple&from=2019-04-24&to=2019-04-24'
        url += '&sortBy=popularity'
        url += `pageSize=${pageSize}`
        url += '&apiKey=318272093cec43d480e5dbe696027306'
    }
}