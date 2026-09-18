import type {Metadata} from 'next';
import PropertyBrowser from '../components/PropertyBrowser';
export const metadata:Metadata={title:'Properties',description:'Interactive sample listings for the Juniper Row Realty portfolio demo.'};
export default function Page(){return <><section className="pageHero pageHero--properties container"><p className="eyebrow">Current selection</p><h1>Properties</h1><p>Filter the sample inventory by property type. Each listing is fictional and exists to demonstrate a real browsing pattern.</p></section><section className="container"><PropertyBrowser/></section></>}
