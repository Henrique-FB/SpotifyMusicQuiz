import { Routes } from '@angular/router';
import { MainscreenComponent } from './features/mainscreen/mainscreen.component';


export const routes: Routes = [
    {
        path: "",
        redirectTo: "mainscreen",
        pathMatch: "full"
    },
    {
        path: "mainscreen",
        component: MainscreenComponent
    }
];
