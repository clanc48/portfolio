"use client";
import {useState} from 'react';
const listings=[
{name:'Juniper House',area:'Juniper District',type:'House',price:'$845,000',meta:'3 bd · 2.5 ba · 2,480 sq ft'},
{name:'Alder Row',area:'Old Market',type:'House',price:'$1,280,000',meta:'4 bd · 3.5 ba · 3,240 sq ft'},
{name:'River Loft 4C',area:'River Ward',type:'Condo',price:'$620,000',meta:'2 bd · 2 ba · 1,420 sq ft'},
{name:'Fieldstone Modern',area:'North Ridge',type:'House',price:'$975,000',meta:'4 bd · 3 ba · 2,910 sq ft'}
];
export default function PropertyBrowser(){
 const [filter,setFilter]=useState('All');
 const shown=filter==='All'?listings:listings.filter(x=>x.type===filter);
 return <><div className="filterBar" aria-label="Filter properties">{['All','House','Condo'].map(x=><button type="button" key={x} aria-pressed={filter===x} onClick={()=>setFilter(x)}>{x}</button>)}</div><div className="browseGrid">{shown.map(x=><article className="listingCard" key={x.name}><div className="listingImage" aria-hidden="true"></div><div className="listingBody"><p className="eyebrow">{x.area}</p><h2>{x.name}</h2><div className="listingMeta"><strong>{x.price}</strong><span>{x.meta}</span></div></div></article>)}</div></>
}