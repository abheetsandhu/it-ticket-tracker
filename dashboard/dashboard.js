const byId = id => document.getElementById(id)
const tickets = [
  {id:101, issue:'Payroll printer offline', owner:'Finance', priority:'High', status:'Open'},
  {id:102, issue:'Meeting room display flickers', owner:'Operations', priority:'Medium', status:'In progress'},
  {id:103, issue:'New hire needs email access', owner:'People team', priority:'High', status:'In progress'},
  {id:104, issue:'Replace keyboard', owner:'Reception', priority:'Low', status:'Closed'}
]
const statuses = ['Open','In progress','Closed']
function renderQueue() {
  const filter = byId('filter').selectedIndex
  const visible = tickets.filter(t => filter===0 || (filter===1 ? t.priority==='High' && t.status!=='Closed' : t.status==='Closed'))
  byId('counts').textContent = statuses.map(s=>tickets.filter(t=>t.status===s).length+' '+s.toLowerCase()).join('  ·  ')
  byId('queue').innerHTML = visible.map(t=>'<details><summary>'+t.issue+'<small>'+t.priority+' priority · '+t.status+'</small></summary><p>#'+t.id+' · '+t.owner+'</p><label for="status'+t.id+'">Ticket status</label><select id="status'+t.id+'" data-id="'+t.id+'">'+statuses.map(s=>'<option '+(s===t.status?'selected':'')+'>'+s+'</option>').join('')+'</select></details>').join('') || '<p>No tickets match this filter.</p>'
}
byId('filter').onchange = () => {byId('feedback').textContent='';renderQueue()}
byId('queue').onchange = e => {
  const ticket = tickets.find(t=>t.id===Number(e.target.dataset.id))
  if (!ticket) return
  ticket.status = e.target.value
  renderQueue()
  byId('feedback').textContent = ticket.issue+' updated to '+ticket.status.toLowerCase()+'.'
  const updated = byId('status'+ticket.id)
  if (updated) {updated.closest('details').open=true;updated.focus()} else byId('filter').focus()
}
renderQueue()
