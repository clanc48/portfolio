import type {Metadata} from 'next';
import type {ReactNode} from 'react';
import Link from 'next/link';
import './globals.css';
export const metadata:Metadata={title:{default:'Juniper Row Realty',template:'%s | Juniper Row Realty'},description:'Portfolio-demo residential real estate brand focused on homes, neighborhoods, and thoughtful representation.'};
const nav=[['Properties','/properties'],['Neighborhoods','/neighborhoods'],['Agents','/agents']] as const;
export default function RootLayout({children}:{children:ReactNode}){
 const schema={"@context":"https://schema.org","@type":"RealEstateAgent","name":"Juniper Row Realty","description":"Portfolio demo real-estate brand.","url":"https://example.com/"};
 return <html lang="en"><body><a className="skipLink" href="#main">Skip to content</a><header className="header container"><Link className="brand" href="/">JUNIPER ROW<small>REALTY</small></Link><nav aria-label="Primary" className="nav">{nav.map(([l,h])=><Link key={h} href={h}>{l}</Link>)}</nav><Link className="button" href="/contact">Talk with an agent</Link></header><main id="main">{children}</main><footer className="footer container"><div><strong>Juniper Row Realty</strong><p>A more thoughtful way home.</p></div><div>Portfolio demo · not a real brokerage</div></footer><script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify(schema)}} /></body></html>
}