import type {Metadata} from 'next';
import type {ReactNode} from 'react';
import Link from 'next/link';
import './globals.css';
export const metadata:Metadata={title:{default:'Redline Motorworks',template:'%s | Redline Motorworks'},description:'Portfolio-demo performance automotive shop focused on diagnostics, measured upgrades, and complete builds.'};
const nav=[['Services','/services'],['Builds','/builds'],['Performance','/performance']] as const;
export default function RootLayout({children}:{children:ReactNode}){
 const schema={"@context":"https://schema.org","@type":"AutoRepair","name":"Redline Motorworks","description":"Portfolio demo automotive performance brand.","url":"https://example.com/"};
 return <html lang="en"><body><a className="skipLink" href="#main">Skip to content</a><header className="header container"><Link className="brand" href="/"><span>R</span>EDLINE MOTORWORKS</Link><nav aria-label="Primary" className="nav">{nav.map(([l,h])=><Link key={h} href={h}>{l}</Link>)}</nav><Link className="button" href="/book-service">Book service</Link></header><main id="main">{children}</main><footer className="footer container"><div>REDLINE MOTORWORKS</div><div>Portfolio demo · not a real automotive shop</div></footer><script type="application/ld+json" dangerouslySetInnerHTML={{__html:JSON.stringify(schema)}} /></body></html>
}