//TODO: Update environment files with correct APIs
import axios from 'axios';

export default class API {
    constructor({ url, name }) {
        this.url = url
        this.name = name
        this.endpoints = this.createEndPoints({ name: this.name })
    }
    createEndPoints({ name }) {
        var endpoints = {}
        const resourceUrl = `${this.url}/${name}`
        endpoints.getAll = () => axios.get(resourceUrl)
        endpoints.getOne = ({ id }) => axios.get(`${resourceUrl}/${id}`)

        //add more endpoints
        return endpoints
    }
}