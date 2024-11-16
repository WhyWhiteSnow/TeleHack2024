import Authorisation from "@/pages/Authorisation.vue"
import TerminalActionPage from "@/pages/TerminalActionPage.vue";
import SupportActionPage from "@/pages/SupportActionPage.vue";



import { createRouter, createWebHistory } from "vue-router"


const routes = [
    {
        path: '/',
        component: Authorisation
    },
    {
        path: '/terminal',
        component: TerminalActionPage
    },
    {
        path: '/support',
        component: SupportActionPage
    }
]

const router = createRouter({
    routes,
    history: createWebHistory()
})

export default router;