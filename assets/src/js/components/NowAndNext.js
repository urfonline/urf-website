import React from 'react';
import { getOnAirSlot } from '../utils/schedule';

function launchPlayer() {
  window.open(
    '/player',
    'URF Player',
    'height=425,width=300,status=yes,toolbar=no,menubar=no'
  );
}

function NowAndNext(props) {
  if (!props.data) {
    return null;
  }

  const slot = getOnAirSlot(props.data.slots);
  const show = props.data.shows[slot.show];
  return (
    <div className="NowAndNext" onClick={launchPlayer}>
      <div className="NowAndNext__heading">Listen</div>
      <div className="NowAndNext__now">Now: {show.title}</div>
    </div>
  );
}

NowAndNext.propTypes = {
  data: React.PropTypes.object,
};

export default NowAndNext;