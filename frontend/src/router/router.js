import Authorisation from '@/pages/Authorisation.vue'
import TerminalActionPage from '@/pages/TerminalActionPage.vue'
import SupportActionPage from '@/pages/SupportActionPage.vue'
import TerminalCallRequestPage from '@/pages/TerminalCallRequestPage.vue'
import TerminalConnectionRequestPage from '@/pages/TerminalConnectionRequestPage.vue'

import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: Authorisation,
  },
  {
    path: '/terminal',
    component: TerminalActionPage,
  },
  {
    path: '/support',
    component: SupportActionPage,
  },
  {
    path: '/call',
    component: TerminalCallRequestPage,
  },
  {
    path: '/connect',
    component: TerminalConnectionRequestPage,
  },
]

const router = createRouter({
  routes,
  history: createWebHistory(),
})

export default router
