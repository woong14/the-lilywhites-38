from pathlib import Path

path = Path("index.html")
s = path.read_text(encoding="utf-8")

def replace_once(old, new, label):
    global s
    if old not in s:
        raise SystemExit(f"patch target missing: {label}")
    s = s.replace(old, new, 1)

replace_once(
'''  .achievement-item small{display:block;margin-top:3px;font-size:8px;font-weight:700;opacity:.68}
  .profile-empty{padding:20px;text-align:center;color:#7187ad;font-size:10px}
''',
'''  .achievement-item small{display:block;margin-top:3px;font-size:8px;font-weight:700;opacity:.68}
  .achievement-progress{margin-top:8px}
  .achievement-progress-head{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:5px;font-size:8px;font-weight:1000;letter-spacing:.35px;color:#91a8cf}
  .achievement-item.done .achievement-progress-head{color:#b8f5d0}
  .achievement-progress-track{height:7px;border-radius:999px;overflow:hidden;background:#12223d;border:1px solid rgba(102,130,177,.20)}
  .achievement-progress-fill{height:100%;border-radius:999px;background:linear-gradient(90deg,#4c75bd,#72a4f7);transition:width .35s ease}
  .achievement-item.done .achievement-progress-fill{background:linear-gradient(90deg,#3aa46b,#78e3a5)}
  .profile-empty{padding:20px;text-align:center;color:#7187ad;font-size:10px}
''',
"achievement progress css")

replace_once(
'''let sessionSpecialHistory = new Set();
let sessionDraftPicks = [];''',
'''let sessionSpecialHistory = new Set();
let sessionSpecialItemHistory = new Set();
let sessionDraftPicks = [];''',
"special item session state")

replace_once(
'''const LILY_ACHIEVEMENTS = [
  ["first_season","첫 시즌","시즌 1회 완료"],
  ["season_10","단골 감독","시즌 10회 완료"],
  ["champion","챔피언","프리미어리그 우승"],
  ["points_90","90점 클럽","한 시즌 승점 90점 이상"],
  ["first_chemistry","첫 번째 연결","팀캐미 1종 발동"],
  ["chemistry_5","케미스트리스트","서로 다른 팀캐미 5종 발동"],
  ["all_chemistries","완벽한 조합","팀캐미 15종 모두 발동"],
  ["first_special","특별한 한 장","특수카드 1종 획득"],
  ["prime_time","PRIME TIME","PRIME TIME 카드 획득"],
  ["the_legends","THE LEGENDS","THE LEGENDS 카드 획득"],
  ["toty","TOTY","TOTY 카드 획득"],
  ["golden_boot","GOLDEN BOOT","GOLDEN BOOT 카드 획득"],
  ["hero","HERO","HERO 카드 획득"],
  ["world_cup_winner","WORLD CUP WINNER","WORLD CUP WINNER 카드 획득"],
  ["wonder_boy","WONDER BOY","WONDER BOY 카드 획득"]
];''',
'''const SPECIAL_CARD_COLLECTION_TOTALS = {
  "PRIME TIME":14,
  "THE LEGENDS":12,
  "TOTY":20,
  "GOLDEN BOOT":5,
  "HERO":6,
  "WORLD CUP WINNER":3,
  "WONDER BOY":3
};

const SPECIAL_CARD_ACHIEVEMENT_TYPES = {
  prime_time:"PRIME TIME",
  the_legends:"THE LEGENDS",
  toty:"TOTY",
  golden_boot:"GOLDEN BOOT",
  hero:"HERO",
  world_cup_winner:"WORLD CUP WINNER",
  wonder_boy:"WONDER BOY"
};

const LILY_ACHIEVEMENTS = [
  ["first_season","첫 시즌","시즌 1회 완료"],
  ["season_10","단골 감독","시즌 10회 완료"],
  ["champion","챔피언","프리미어리그 우승"],
  ["points_90","90점 클럽","한 시즌 승점 90점 이상"],
  ["first_chemistry","첫 번째 연결","팀캐미 1종 발동"],
  ["chemistry_5","케미스트리스트","서로 다른 팀캐미 5종 발동"],
  ["all_chemistries","완벽한 조합","팀캐미 15종 모두 발동"],
  ["first_special","특별한 한 장","특수카드 1장 획득"],
  ["prime_time","PRIME TIME 컬렉터","PRIME TIME 14장 모두 수집"],
  ["the_legends","THE LEGENDS 컬렉터","THE LEGENDS 12장 모두 수집"],
  ["toty","TOTY 컬렉터","TOTY 20장 모두 수집"],
  ["golden_boot","GOLDEN BOOT 컬렉터","GOLDEN BOOT 5장 모두 수집"],
  ["hero","HERO 컬렉터","HERO 6장 모두 수집"],
  ["world_cup_winner","WORLD CUP WINNER 컬렉터","WORLD CUP WINNER 3장 모두 수집"],
  ["wonder_boy","WONDER BOY 컬렉터","WONDER BOY 3장 모두 수집"]
];

function getSpecialCardProgress(profile, type){
  const prefix = `${type}::`;
  const items = Array.isArray(profile?.special_card_items) ? profile.special_card_items : [];
  const collected = new Set(items.filter(v=>String(v).startsWith(prefix)).map(String)).size;
  const total = Number(SPECIAL_CARD_COLLECTION_TOTALS[type] || 0);
  return {collected,total,percent:total ? Math.min(100,Math.round((collected/total)*100)) : 0};
}''',
"achievement definitions")

replace_once(
'''    <div class="profile-section">
      <div class="profile-section-title">SPECIAL CARD COLLECTION · ${(p.special_cards || []).length}/7</div>
      <div class="profile-chip-list">
        ${(p.special_cards || []).length ? p.special_cards.map(name=>`<span class="profile-chip">${escapeProfileHtml(name)}</span>`).join("") : '<span class="profile-empty">아직 기록된 특수카드가 없습니다.</span>'}
      </div>
    </div>

    <div class="profile-section">
      <div class="profile-section-title">ACHIEVEMENTS · ${LILY_ACHIEVEMENTS.filter(([id])=>achievements.has(id)).length}/${LILY_ACHIEVEMENTS.length}</div>
      <div class="achievement-grid">
        ${LILY_ACHIEVEMENTS.map(([id,name,desc])=>`
          <div class="achievement-item ${achievements.has(id) ? "done" : ""}">
            ${achievements.has(id) ? "✓ " : "□ "}${escapeProfileHtml(name)}
            <small>${escapeProfileHtml(desc)}</small>
          </div>
        `).join("")}
      </div>
    </div>''',
'''    <div class="profile-section">
      <div class="profile-section-title">SPECIAL CARD TYPES · ${(p.special_cards || []).length}/7</div>
      <div class="profile-chip-list">
        ${(p.special_cards || []).length ? p.special_cards.map(name=>`<span class="profile-chip">${escapeProfileHtml(name)}</span>`).join("") : '<span class="profile-empty">아직 기록된 특수카드가 없습니다.</span>'}
      </div>
    </div>

    <div class="profile-section">
      <div class="profile-section-title">ACHIEVEMENTS · ${LILY_ACHIEVEMENTS.filter(([id])=>achievements.has(id)).length}/${LILY_ACHIEVEMENTS.length}</div>
      <div class="achievement-grid">
        ${LILY_ACHIEVEMENTS.map(([id,name,desc])=>{
          const specialType = SPECIAL_CARD_ACHIEVEMENT_TYPES[id];
          const progress = specialType ? getSpecialCardProgress(p,specialType) : null;
          return `
          <div class="achievement-item ${achievements.has(id) ? "done" : ""}">
            ${achievements.has(id) ? "✓ " : "□ "}${escapeProfileHtml(name)}
            <small>${escapeProfileHtml(desc)}</small>
            ${progress ? `
              <div class="achievement-progress">
                <div class="achievement-progress-head"><span>COLLECTION</span><strong>${progress.collected} / ${progress.total}</strong></div>
                <div class="achievement-progress-track"><div class="achievement-progress-fill" style="width:${progress.percent}%"></div></div>
              </div>
            ` : ""}
          </div>`;
        }).join("")}
      </div>
    </div>''',
"profile achievements UI")

replace_once(
'''        chemistries:[...sessionChemistryHistory],
        special_cards:[...sessionSpecialHistory]
      });''',
'''        chemistries:[...sessionChemistryHistory],
        special_cards:[...sessionSpecialHistory],
        special_card_items:[...sessionSpecialItemHistory]
      });''',
"sync payload")

replace_once(
'''function rememberSpecialCardForProfile(player){
  const type = getSpecialCardCollectionType(player);
  if(!type || sessionSpecialHistory.has(type)) return;
  sessionSpecialHistory.add(type);
  queueProfileProgressSync();
}''',
'''function rememberSpecialCardForProfile(player){
  const type = getSpecialCardCollectionType(player);
  if(!type || !player) return;
  const itemKey = `${type}::${pairKey(player.name,player.season)}`;
  let changed = false;
  if(!sessionSpecialHistory.has(type)){
    sessionSpecialHistory.add(type);
    changed = true;
  }
  if(!sessionSpecialItemHistory.has(itemKey)){
    sessionSpecialItemHistory.add(itemKey);
    changed = true;
  }
  if(changed) queueProfileProgressSync();
}''',
"remember individual special cards")

replace_once(
'''        chemistries:[...sessionChemistryHistory],
        special_cards:[...sessionSpecialHistory]
      }
    });''',
'''        chemistries:[...sessionChemistryHistory],
        special_cards:[...sessionSpecialHistory],
        special_card_items:[...sessionSpecialItemHistory]
      }
    });''',
"season payload")

replace_once(
'''  sessionChemistryHistory = new Set();
  sessionSpecialHistory = new Set();
  activeChemistryIds = new Set();''',
'''  sessionChemistryHistory = new Set();
  sessionSpecialHistory = new Set();
  sessionSpecialItemHistory = new Set();
  activeChemistryIds = new Set();''',
"reset item history")

path.write_text(s, encoding="utf-8")
print("Patched index.html for v148")
