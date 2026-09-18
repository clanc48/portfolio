import type { ReactNode } from 'react';
import Link from 'next/link';
const nav = [["Home","/"],["Services","/services"],["Builds","/builds"],["Performance","/performance"],["Book Service","/book-service"]] as const;
export default function RootLayout({children}:{children:ReactNode}){return <html lang='en'><body><header><strong>Redline Motorworks</strong><nav>{nav.map(([label,href])=><Link key={href} href={href} style={{marginRight:16}}>{label}</Link>)}</nav></header>{children}</body></html>}
