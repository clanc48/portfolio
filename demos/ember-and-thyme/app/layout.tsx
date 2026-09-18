import type { ReactNode } from 'react';
import Link from 'next/link';
const nav = [["Home","/"],["Menu","/menu"],["Story","/story"],["Events","/events"],["Reservations","/reservations"]] as const;
export default function RootLayout({children}:{children:ReactNode}){return <html lang='en'><body><header><strong>Ember & Thyme</strong><nav>{nav.map(([label,href])=><Link key={href} href={href} style={{marginRight:16}}>{label}</Link>)}</nav></header>{children}</body></html>}
