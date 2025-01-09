import { SpotifyApi } from '@spotify/web-api-ts-sdk';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';

@Injectable({
    providedIn: 'root',
})

export class SpotifyService {

    scopes: string[] =  ["user-read-private"]
    //sdk: SpotifyApi = SpotifyApi.withClientCredentials(environment.spotifyClient, environment.spotifySecret, this.scopes);
    sdk: SpotifyApi = SpotifyApi.withUserAuthorization(environment.spotifyClient, "http://localhost:4200", this.scopes)
    constructor() {}
}

